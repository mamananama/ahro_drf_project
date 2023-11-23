console.log("Load JS");
import { getToken } from "./auth.js";

// 로딩 되자마자 실행한다. 브라우저 로딩 됐는지 확인할 수 있다.
// 비동기함수 async : ~ 하는 동안 언제 요청이 올지 모르니 다른 거 먼저 실행, await 사용
window.onload = async function loadArticles() {
	// 요청 보내고 돌아오는 것을 저장할 변수. 변경되지 않을 변수 만들 때
	// const token = getToken();
	// console.log(token);
	const response = await fetch("http://127.0.0.1:8000/account/profile/test_account/", {
		method: "GET",
		headers: {
			Authorization:
				"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwNzE4OTgxLCJpYXQiOjE3MDA3MTUzODEsImp0aSI6IjdiMThkOTgzNzE1OTRkMzNhZjFjMjIwMjE2YTcwODM5IiwidXNlcl9pZCI6Mn0.mhyB3W9uMiBcv8sFBCROTJZ_b5mA82BThBATikwlP7s",
		},
	});
	// await : 이 요청 보내고 기다릴 것. 돌아오면 response에 저장.
	// 더 자세하게 {header부분}. default는 'GET'이지만 적어준다.
	// 이 주소로, 'GET' 방식으로 보내고, 돌아오는 값을 response에 저장한다.

	// 시리얼라이즈 상태로 받아온 것을 -> js object 형태로 쓰기 위해
	const response_json = await response.json();
	console.log(response_json);
};
