from transformers import pipeline


# Global variable to hold the model pipeline
text_generator = None


def load_model():
    """
    Load the GPT-2 model pipeline for text generation.
    This function should be called once at startup.
    """
    global text_generator
    if text_generator is None:
        print("Loading GPT-2 model...")
        text_generator = pipeline(
            "text-generation",
            model="gpt2",
            device=-1  # Use CPU; change to 0 for GPU if available
        )
        print("Model loaded successfully.")
    return text_generator


def generate_text(prompt: str, max_length: int = 100, temperature: float = 0.7, top_k: int = 50, top_p: float = 0.9) -> str:
    """
    Generate text based on the input prompt using the loaded model.

    Args:
        prompt (str): The input prompt for generation.
        max_length (int): Maximum length of the generated text.
        temperature (float): Sampling temperature.
        top_k (int): Top-k sampling parameter.
        top_p (float): Top-p (nucleus) sampling parameter.

    Returns:
        str: The generated text response.
    """
    if text_generator is None:
        raise RuntimeError("Model not loaded. Call load_model() first.")

    # Generate text
    outputs = text_generator(
        prompt,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        num_return_sequences=1,
        do_sample=True,
        pad_token_id=text_generator.tokenizer.eos_token_id
    )

    # Extract the generated text (remove the original prompt)
    generated_text = outputs[0]['generated_text']
    if generated_text.startswith(prompt):
        response = generated_text[len(prompt):].strip()
    else:
        response = generated_text.strip()

    return response
