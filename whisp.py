import openai
import whisper
import datetime
import ffmpeg
import subprocess
from moviepy.editor import VideoFileClip
import torch
# import pyannote.audio
# from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
# embedding_model = PretrainedSpeakerEmbedding(
#     "speechbrain/spkrec-ecapa-voxceleb",
#     device=torch.device("cuda"))
#
# from pyannote.audio import Audio
# from pyannote.core import Segment
#
# import wave
# import contextlib
#
# from sklearn.cluster import AgglomerativeClustering
# import numpy as np
KEY='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'
openai.api_key = KEY


#============================================================================

# Вариант 1: AttributeError: module 'openai' has no attribute 'Whisper' не находит Whisper. хотя вроде все библиотеки есть. пока не нашел норм ответа на форумах и сайтаз
# def transcribe_audio(file_path):
#     with open(file_path, 'rb') as f:
#         data = f.read()
#
#     response = openai.Whisper.transcribe(data)
#     return response['transcription']
#
# # path_to_audio_file should be replaced with the path to the audio file extracted from your video
# transcription = transcribe_audio('/Users/mymacbook/PycharmProjects/pythonProject/openai_whisper/1.mp4')
# print(transcription)

#===================================================================================================

#ЗДЕСЬ Я ПЕРЕКОДИРОВАЛ ФОРМАТ В MP4 ПОТОМУ ЧТО НЕ ЧИТАЛА MOV

# input_file = "/Users/mymacbook/PycharmProjects/pythonProject/openai_whisper/1.mov"
# output_file = "/Users/mymacbook/PycharmProjects/pythonProject/openai_whisper/1.mp4"

# stream = ffmpeg.input(input_file)
# stream = ffmpeg.output(stream, output_file)
# ffmpeg.run(stream)
# Создаем объект VideoFileClip, загружая видео .mov
# clip = VideoFileClip('/Users/mymacbook/PycharmProjects/pythonProject/openai_whisper/1.mov')
#
# # Записываем видео в новый формат (.mp4)
# clip.write_videofile('/Users/mymacbook/PycharmProjects/pythonProject/openai_whisper/1.mp4')

#================================================================================


# вариант 2: он сработал. хотя и на англ.но сработал
# def transcribe_audio(file_path):
#
#     with open(file_path, 'rb') as f:
#         response = openai.Audio.transcribe(
#                 api_key=KEY,
#                 model='whisper-1',
#                 file=f,
#                 response_format='text'
#             )
#     return response
#
# print(transcribe_audio('/Users/mymacbook/PycharmProjects/pythonProject/openai_whisper/1.mp4'))
path = '/Users/mymacbook/PycharmProjects/pythonProject/openai_whisper/1.mp4'
model = whisper.load_model('base.en')
option = whisper.DecodingOptions(Language='ru', fp16=False)
result = model.transcribe(path)

print(result['text'])#должен быть ключ text

save_target = 'transcribe.txt'

with open(save_target, 'w') as f:
    for index, segment in enumerate(result['segments']):
        f.write(str(index + 1) + '\n')
        f.write(str(datetime.timedelta(seconds=segment['start'])) + '-->' + str(datetime.timedelta(seconds=segment['end'])) + '\n')
        f.write(segment['text'].strip() + '\n')
        f.write('\n')
# еще варик
#     for (i, segment) in enumerate(result['segments']):
#         if i == 0 or result['segments'][i - 1]["speaker"] != segment["speaker"]:
#             f.write("\n" + segment["speaker"] + ' ' + str(time(segment["start"])) + '\n')
#         f.write(segment["text"][1:] + ' ')
