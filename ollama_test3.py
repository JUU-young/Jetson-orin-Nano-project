import requests

url = "http://127.0.0.1:11434/api/generate"

# 사용자에게 나라 이름 입력받기
country = input("알고 싶은 나라 이름을 입력하세요: ")

prompt = f"""
너는 국가 정보를 정리해주는 assistant야.

사용자가 질문한 나라:
- 나라 이름: {country}

아래 형식으로만 한국어로 출력해.

[국가 요약]
{country}가 어떤 나라인지 한 문장으로 설명해.

[수도]
{country}의 수도를 출력해.

[현 지도자]
{country}의 현재 지도자를 출력해.

[GDP]
{country}의 GDP를 출력해. 가능하면 최신 기준 연도도 함께 적어.

[인구수]
{country}의 인구수를 출력해. 가능하면 기준 연도도 함께 적어.

[면적]
{country}의 면적을 출력해.

[주의]
정보가 최신이 아닐 수 있으면 그 점을 한 문장으로 설명해.
"""

data = {
    "model": "gemma3:1b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=data)
response.raise_for_status()

result = response.json()

print("\n=== 국가 정보 출력 ===")
print(result["response"])