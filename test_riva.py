import grpc
import riva.client

auth = riva.client.Auth(
    uri="grpc.nvcf.nvidia.com:443",
    use_ssl=True,
    metadata_args=[
        ("function-id", "b702f636-f60c-4a3d-a6f4-f3568c13bd7d"),
        ("authorization", "Bearer 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")
    ]
)

try:
    asr_service = riva.client.ASRService(auth)
    
    with open("test.wav", "rb") as f:
        audio_chunk = f.read()

    config = riva.client.RecognitionConfig()
    config.language_code = "it-IT"
    config.max_alternatives = 1
    config.enable_automatic_punctuation = True

    response = asr_service.offline_recognize(audio_chunk, config)
    print("Transcription Response:", response)
except Exception as e:
    print("Error:", e)
