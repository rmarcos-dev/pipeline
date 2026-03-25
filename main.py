from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Control Panel | AppSur</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            :root { --bg: #0b0e14; --card: #161b22; --accent: #238636; --text: #c9d1d9; }
            body { font-family: 'Inter', sans-serif; background-color: var(--bg); color: var(--text); margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
            .dashboard { width: 90%; max-width: 800px; background: var(--card); border: 1px solid #30363d; border-radius: 12px; padding: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
            .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #30363d; padding-bottom: 1rem; margin-bottom: 2rem; }
            .status-dot { width: 12px; height: 12px; background: #2ea043; border-radius: 50%; display: inline-block; margin-right: 8px; box-shadow: 0 0 10px #2ea043; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; }
            .card { background: #0d1117; border: 1px solid #30363d; padding: 1.5rem; border-radius: 8px; text-align: center; transition: transform 0.2s; }
            .card:hover { transform: translateY(-5px); border-color: var(--accent); }
            .card h3 { margin: 0; font-size: 0.9rem; color: #8b949e; text-transform: uppercase; }
            .card p { font-size: 1.5rem; font-weight: 600; margin: 10px 0 0; color: #f0f6fc; }
            .footer { margin-top: 2rem; text-align: center; font-size: 0.8rem; color: #484f58; }
            .pulse { animation: pulse-animation 2s infinite; }
            @keyframes pulse-animation { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <div class="header">
                <div>
                    <h2 style="margin:0">AppSur <span style="font-weight:300">Container</span></h2>
                    <p style="margin:5px 0 0; font-size:0.8rem; color:#8b949e">Cloudflare Tunnel: Active</p>
                </div>
                <div style="text-align: right">
                    <span class="status-dot pulse"></span> <span style="font-size: 0.9rem; font-weight:600">SISTEMA LIVE</span>
                </div>
            </div>
            
            <div class="grid">
                <div class="card">
                    <h3>Deployment</h3>
                    <p>CI/CD ✅</p>
                </div>
                <div class="card">
                    <h3>Runner</h3>
                    <p>Self-Hosted</p>
                </div>
                <div class="card">
                    <h3>Network</h3>
                    <p>Encrypted</p>
                </div>
            </div>

            <div class="footer">
                &copy; 2026 rmarcos-dev - Desplegado desde Windows vía GitHub Actions
            </div>
        </div>
    </body>
    </html>
    """
