from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/call', methods=['POST'])
def make_call():
    # Get the phone number from the request
    phone_number = request.json.get('number')
    if not phone_number:
        return "Error: No phone number provided", 400

    # Use ADB to make the call
    try:
        # Reconnect to the device if necessary
        subprocess.run(['adb', 'connect', '192.168.68.107:5555'], capture_output=True, text=True)

        # Make the call
        result = subprocess.run(
            ['adb', '-s', '192.168.68.107:5555', 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d', f'tel:{phone_number}'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return f"Calling {phone_number}"
        else:
            return f"Error: {result.stderr}", 500
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)