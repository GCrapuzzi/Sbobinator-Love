export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const chunks = [];
    for await (const chunk of req) {
      chunks.push(chunk);
    }
    const buffer = Buffer.concat(chunks);

    const formData = new FormData();
    const blob = new Blob([buffer], { type: req.headers['content-type'] || 'application/octet-stream' });
    formData.append("file", blob, "uploaded_audio");
    formData.append("model", "openai/whisper-large-v3");
    formData.append("language", "it");

    const nimRes = await fetch("https://ai.api.nvidia.com/v1/audio/transcriptions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${process.env.NVIDIA_API_KEY}`
      },
      body: formData
    });

    if (!nimRes.ok) {
      const errText = await nimRes.text();
      console.error("NVIDIA API Error:", nimRes.status, errText);
      return res.status(nimRes.status).json({ error: "Errore API NVIDIA", details: errText });
    }

    const data = await nimRes.json();
    return res.status(200).json(data);

  } catch (error) {
    console.error("Vercel Function Error:", error);
    return res.status(500).json({ error: "Errore interno del server" });
  }
}
