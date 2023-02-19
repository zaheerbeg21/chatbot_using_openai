from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files['file-input']
    # save the file to the database or filesystem

def generate_response(user_input):
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_output = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    bot_response = tokenizer.decode(bot_output[0], skip_special_tokens=True)
    return bot_response


@app.route('/api/chat', methods=['POST'])
def chat():
    question = request.form['question-input']
    # process the question and generate a response
    response = generate_response(question)
    return jsonify(response)

if __name__ == '__main__':
    app.run()
