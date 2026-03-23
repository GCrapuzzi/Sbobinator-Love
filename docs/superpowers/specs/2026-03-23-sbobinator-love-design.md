# Design Spec: Sbobinator Love

## 1. Goal
A very simple, single-page web application designed for the user's girlfriend to easily upload audio files from an iOS device and receive an Italian transcription using the NVIDIA NIM Whisper Large v3 model.

## 2. Architecture & Tech Stack
- **Frontend**: Single `index.html` file (with embedded or separate CSS/JS) avoiding any build tools for maximum simplicity and instant activation.
- **Hosting**: Deployed as static files on Vercel or GitHub Pages. Zero maintenance. 
- **API Communication**: The frontend makes direct HTTP `fetch` calls to the NVIDIA NIM endpoint (`https://ai.api.nvidia.com/v1/audio/transcriptions`).
- **Security**: The API key is hardcoded into the client-side JavaScript. (User explicitly indicated this is a private app and security concerns around the key exposure are disregarded).

## 3. User Interface (UI)
- **Mobile-First Design (iOS/iPadOS Target)**: The entire interface will be strictly optimized for Safari on iPhone and iPad. This means large touch-friendly tap targets, readable typography without zooming, viewport meta tags to prevent accidental scaling, and an interface that avoids horizontal scrolling.
- **Visual Style**: "Playful & Card-based" (Giocoso a schede). Central card layout with soft, rounded edges, and pastel colors.
- **Components**:
  - A friendly file input area labeled "Carica l'audio ❤️".
  - A subtle loading state showing neutral but affectionate text (e.g., "Sto sbobinando questo file per te...").
  - A result area displaying the transcribed text in an elegant, easily copyable block.
- **Tone**: Affectionate but NOT overly romantic/cheesy. The word "tesoro" is strictly prohibited. Use simple positive reinforcements (e.g., "Ecco la tua trascrizione!").

## 4. Workflows
- **Audio Upload**: Tap the button -> iOS file picker or voice memo selection -> JavaScript intercepts file -> File is sent to NVIDIA API via multipart/form-data.
- **Loading State**: UI shows loading text.
- **Success State**: Displays transcription.
- **Error State**: Displays a friendly fallback message ("Ops, c'è stato un piccolo intoppo tecnico, riproviamo?").

## 5. Next Steps
Move to implementation via the `writing-plans` skill to formalize the code steps.
