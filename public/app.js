document.querySelector("#msg").textContent =
    "網址如果長得像 http://localhost:8080/，你就是在跟伺服器互動。";

document.querySelector("#btn").addEventListener("click", () => {
    alert("前端 JS 正常運作 ✅");
});
