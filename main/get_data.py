from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Spring Boot 서버의 URL을 설정합니다.
SPRING_BOOT_URL = "http://localhost:8080/api/search"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # HTML 폼에서 입력한 데이터를 가져옵니다.
        team = request.form.get("team")
        what = request.form.get("what")

        # Spring Boot 서버로 POST 요청을 보냅니다.
        response = requests.post(SPRING_BOOT_URL, data={"team": team, "what": what})

        if response.status_code == 200:
            # JSON 형식의 문자열을 파이썬 딕셔너리로 파싱
            data = json.loads(response.text)

            # json.dumps() 함수를 사용하여 예쁘게 출력 (들여쓰기 포함)
            result = json.dumps(data, indent=4, ensure_ascii=False)
        else:
            result = "데이터가 없습니다"  # 오류 처리

        return render_template("index.html", result=result)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
