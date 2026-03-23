from http.server import BaseHTTPRequestHandler
import json
import grpc
import riva.client
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            audio_chunk = self.rfile.read(content_length)

            api_key = os.environ.get('NVIDIA_API_KEY', '')

            auth = riva.client.Auth(
                uri="grpc.nvcf.nvidia.com:443",
                use_ssl=True,
                metadata_args=[
                    ("function-id", "b702f636-f60c-4a3d-a6f4-f3568c13bd7d"),
                    ("authorization", f"Bearer {api_key}")
                ]
            )

            asr_service = riva.client.ASRService(auth)
            config = riva.client.RecognitionConfig()
            config.language_code = "it-IT"
            config.max_alternatives = 1
            config.enable_automatic_punctuation = True

            response = asr_service.offline_recognize(audio_chunk, config)
            
            transcript = ""
            if response and response.results:
                for result in response.results:
                    if len(result.alternatives) > 0:
                        transcript += result.alternatives[0].transcript
                    
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"text": transcript.strip()}).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
