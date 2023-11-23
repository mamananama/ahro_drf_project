export async function refreshToken() {
	const response = await fetch("/api/token/refresh/", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ refresh: "your_refresh_token_here" }),
	});

	const data = await response.json();
	if (!response.ok) {
		throw new Error("Token refresh failed");
	}

	// 새로운 액세스 토큰 저장
	localStorage.setItem("access_token", data.access);

	return data.access;
}

export function getToken() {
	const accessToken = localStorage.getItem("access_token");
	if (!accessToken) {
		throw new Error("Access token not found");
	}

	const payload = JSON.parse(atob(accessToken.split(".")[1]));
	const exp = payload.exp;
	const now = Date.now() / 1000;

	// 토큰이 만료되면 새로운 토큰을 요청
	if (now > exp) {
		return refreshToken();
	}

	return Promise.resolve(accessToken);
}
