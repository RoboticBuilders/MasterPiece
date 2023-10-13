from transformers import BarkModel, AutoProcessor
import scipy

device = "cpu"
model = BarkModel.from_pretrained("suno/bark-small")
model = model.to(device)

processor = AutoProcessor.from_pretrained("suno/bark")

voice_preset = "v2/en_speaker_9"
text_prompt = "Starry Night is perhaps the most famous painting by Vincent Van Gogh. The oil-on-canvas painting is dominated by a night sky roiling with chromatic blue swirls, a glowing yellow crescent moon, and stars rendered as radiating orbs. One or two cypress trees, often described as flame-like, tower over the foreground to the left, their dark branches curling and swaying to the movement of the sky that they partly obscure."
inputs = processor(text_prompt, voice_preset=voice_preset)

# generate speech
speech_output = model.generate(**inputs.to(device))

sampling_rate = model.generation_config.sample_rate
scipy.io.wavfile.write("bark_out.wav", rate=sampling_rate, data=speech_output[0].cpu().numpy())