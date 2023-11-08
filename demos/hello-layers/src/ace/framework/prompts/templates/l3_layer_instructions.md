{{ace_context}}
{{identity}}

Below is a list of your incoming messages.

# INCOMING MESSAGES

## TELEMETRY MESSAGES
{{telemetry}}

## NORTH BUS

### DATA MESSAGES
{{data}}

### DATA_RESPONSE MESSAGES
{{data_resp}}

### DATA_REQUEST MESSAGES
{{data_req}}

## SOUTH BUS

### CONTROL MESSAGES
{{control}}

### CONTROL_RESPONSE MESSAGES
{{control_resp}}

### CONTROL_REQUEST MESSAGES
{{control_req}}

# RESPONSE 

Request message types require immediate response. Each message of type DATA_REQUEST requires you to respond to the request with a message of type CONTROL_RESPONSE.
Similarly, each message of type CONTROL_REQUEST requires you to respond to the request with a message of type DATA_RESPONSE.
Your responses should use "question in answer" format.

{{control_operation_prompt}}

{{data_operation_prompt}}

{{history}}

## FORMAT 

Your response should be an array of messages with type, direction and message attributes no other fields. Include only this array and no other text. For example if you want to send one DATA_REQUEST message and one CONTROL message:
[
    {
        "type": "DATA_RESPONSE",
        "direction": "northbound",
        "message": "We do not currently have access to the linkedin API"
    },
    {
        "type": "CONTROL",
        "direction": "southbound",
        "message": "The user requested assistance in booking his flight. You may use our web searching tool "corgi" to find a suitable flight for him/"
    }
]
