from openai import OpenAI
client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key="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")
try:
    print(client.audio.transcriptions.create(file=open("test.wav", "rb"), model="openai/whisper-large-v3"))
except Exception as e:
    print("Error:", e)
