# import requests
# login_url = 'https://api.zerogpt.com/api/auth/login'
# ZEROGPT_API_KEY='4c36e744-9829-4446-816f-f5b101a27986'
# ZEROGPT_EMAIL='lijia.tong@oneclass.com'
# ZEROGPT_PASSWORD='tonglijia.'

# data = {
#     'email': ZEROGPT_EMAIL,
#     'password': ZEROGPT_PASSWORD
# }
# login_headers = {
#     'Content-Type': 'application/json',
# }
# headers = {
#     'Content-Type': 'application/json',
#     'ApiKey': ZEROGPT_API_KEY,
# }
# response = requests.post(login_url, json=data, headers=login_headers)
# json_response = response.json()
# if json_response['success']:
#     token = json_response['data']['token']
#     headers['Authorization'] = 'Bearer ' + token
#     print(headers)
#     data = {
#         'input_text': txt
#     }
#     url = 'https://api.zerogpt.com/api/detect/detectText'
#     response = requests.post(url, json=data, headers=headers)
#     json_response = response.json()
    
#     print(response.json())



import re

origin_text = "Numerous successful cultural exchange initiatives serve as models for promoting global understanding. For example, the Fulbright Program facilitates academic and cultural exchange between the United States and other countries, fostering mutual understanding and collaboration. The Japan Exchange and Teaching Program (JET) promotes internationalization by placing native English speakers in Japanese schools. These initiatives provide participants with opportunities to immerse themselves in different cultures, learn new languages, and build lifelong connections."

h = [
  "initiatives serve as models for promoting",
  "exchange between the United States and other countries",
]

# 为 h 中的每个元素添加 HTML 标签
h_with_tags = [f'<span style="color: #f4d338">{text}</span>' for text in h]

# 创建一个将原始文本和标签对应的字典
replacement_dict = dict(zip(h, h_with_tags))

# 在原始文本中替换相应的文本
for original, replacement in replacement_dict.items():
    origin_text = re.sub(re.escape(original), replacement, origin_text)

print(origin_text)