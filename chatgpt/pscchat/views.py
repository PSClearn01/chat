from django.shortcuts import render
from django.http import JsonResponse
import requests


def index(requests):
    return render(requests, 'index.html')

        
#         answer = response.text
#         return JsonResponse({'response': answer})

url = "https://api.edenai.run/v2/text/chat"

payload = {
    "temperature": 0,
    "max_tokens": 1000,
    "providers": ["anthropic/claude-instant-v1"]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOWM2YTZhY2ItYjVkYi00NTNmLWE1ZTctMTQ3ZTg4NjdhNjEyIiwidHlwZSI6InNhbmRib3hfYXBpX3Rva2VuIn0.jPRbf3i3rGWj_I3n0ekr8CQFF6BOZbEzZN1krVtJtnE"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

# Create your views here.

#     return JsonResponse({'response': 'Invalid request'}, status=500)
        
          
        
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo-instruct",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": message}
#             ],
            
#         )
        
#         answer = completion.choices[0].message.content
#         return JsonResponse({'response': answer})
#     return headers({'response': 'Invalid request'}, status=400)