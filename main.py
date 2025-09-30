from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime

# Initialize FastAPI app
app = FastAPI()

# Define the request model for the /hello endpoint
class HelloRequest(BaseModel):
    name: str


# GET /ping endpoint
@app.get("/ping")
async def ping():
    return {"message": "pong"}

# POST /hello endpoint
@app.post("/hello")
async def hello(request: HelloRequest):
    # Get current timestamp
    timestamp = datetime.now().isoformat()
    # Create response message
    message = f"Hello, {request.name}! Timestamp: {timestamp}"
    return {"message": message}


# Default route (GET /) with instructions
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>ProvableMarkets API Documentation</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    padding: 20px;
                }
                
                .container {
                    max-width: 900px;
                    margin: 0 auto;
                    background: rgba(255, 255, 255, 0.95);
                    border-radius: 15px;
                    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
                    backdrop-filter: blur(10px);
                    overflow: hidden;
                }
                
                .header {
                    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                    color: white;
                    padding: 40px 30px;
                    text-align: center;
                }
                
                .header h1 {
                    font-size: 2.5rem;
                    margin-bottom: 10px;
                    font-weight: 600;
                }
                
                .header p {
                    font-size: 1.1rem;
                    color: white;
                    opacity: 1;
                }
                
                .content {
                    padding: 30px;
                }
                
                .endpoints-section {
                    margin-bottom: 30px;
                }
                
                .endpoint-card {
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 15px;
                    transition: transform 0.2s, box-shadow 0.2s;
                }
                
                .endpoint-card:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
                }
                
                .endpoint-method {
                    display: inline-block;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-weight: bold;
                    font-size: 0.85rem;
                    text-transform: uppercase;
                    margin-right: 10px;
                }
                
                .get-method {
                    background: #10b981;
                    color: white;
                }
                
                .post-method {
                    background: #f59e0b;
                    color: white;
                }
                
                .endpoint-path {
                    font-family: 'Courier New', monospace;
                    font-weight: bold;
                    color: #4f46e5;
                }
                
                h2 {
                    color: #1f2937;
                    margin: 30px 0 15px 0;
                    font-size: 1.5rem;
                    border-bottom: 2px solid #e5e7eb;
                    padding-bottom: 10px;
                }
                
                h3 {
                    color: #374151;
                    margin: 25px 0 10px 0;
                    font-size: 1.2rem;
                }
                
                p {
                    margin-bottom: 15px;
                    color: #4b5563;
                }
                
                pre {
                    background: #1f2937;
                    color: #f9fafb;
                    padding: 15px;
                    border-radius: 8px;
                    font-family: 'Courier New', monospace;
                    overflow-x: auto;
                    margin: 15px 0;
                    font-size: 0.9rem;
                }
                
                code {
                    background: #f3f4f6;
                    color: #1f2937;
                    padding: 2px 6px;
                    border-radius: 4px;
                    font-family: 'Courier New', monospace;
                    font-size: 0.9rem;
                }
                
                a {
                    color: #4f46e5;
                    text-decoration: none;
                    font-weight: 500;
                    transition: color 0.2s;
                }
                
                a:hover {
                    color: #7c3aed;
                    text-decoration: underline;
                }
                
                .form-section {
                    background: #f8fafc;
                    border-radius: 10px;
                    padding: 25px;
                    margin: 20px 0;
                    border: 1px solid #e2e8f0;
                }
                
                .form-group {
                    margin-bottom: 20px;
                }
                
                label {
                    display: block;
                    margin-bottom: 8px;
                    font-weight: 600;
                    color: #374151;
                }
                
                input[type="text"] {
                    width: 100%;
                    padding: 12px 15px;
                    border: 2px solid #d1d5db;
                    border-radius: 8px;
                    font-size: 1rem;
                    transition: border-color 0.2s, box-shadow 0.2s;
                    background: white;
                }
                
                input[type="text"]:focus {
                    outline: none;
                    border-color: #4f46e5;
                    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
                }
                
                button {
                    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                    color: white;
                    border: none;
                    padding: 12px 25px;
                    border-radius: 8px;
                    font-size: 1rem;
                    font-weight: 600;
                    cursor: pointer;
                    transition: transform 0.2s, box-shadow 0.2s;
                }
                
                button:hover {
                    transform: translateY(-1px);
                    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
                }
                
                button:active {
                    transform: translateY(0);
                }
                
                .response-section {
                    margin-top: 20px;
                    padding: 15px;
                    background: #f9fafb;
                    border-radius: 8px;
                    border-left: 4px solid #4f46e5;
                }
                
                .response-label {
                    font-weight: 600;
                    color: #374151;
                    margin-bottom: 8px;
                }
                
                .response-content {
                    font-family: 'Courier New', monospace;
                    background: white;
                    padding: 10px;
                    border-radius: 6px;
                    border: 1px solid #e5e7eb;
                    min-height: 40px;
                    display: flex;
                    align-items: center;
                    color: #4b5563;
                }
                
                .success {
                    color: #059669;
                }
                
                .error {
                    color: #dc2626;
                }
                
                @media (max-width: 768px) {
                    body {
                        padding: 10px;
                    }
                    
                    .header h1 {
                        font-size: 2rem;
                    }
                    
                    .content {
                        padding: 20px;
                    }
                    
                    pre {
                        font-size: 0.8rem;
                        padding: 10px;
                    }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>ProvableMarkets API</h1>
                    <p>Simple API - modified 30/09/2025 13:28 </p>
                </div>
                
                <div class="content">
                    <div class="endpoints-section">
                        <h2>Available Endpoints</h2>
                        
                        <div class="endpoint-card">
                            <div>
                                <span class="endpoint-method get-method">GET</span>
                                <span class="endpoint-path">/ping</span>
                            </div>
                            <p style="margin-top: 10px;">Returns {"message": "pong"} - useful for testing if the server is running. 
                            <a href="/ping">Try it</a></p>
                        </div>
                        
                        <div class="endpoint-card">
                            <div>
                                <span class="endpoint-method post-method">POST</span>
                                <span class="endpoint-path">/hello</span>
                            </div>
                            <p style="margin-top: 10px;">Send a JSON with your name and get a greeting back with timestamp.</p>
                        </div>
                    </div>

                    <h2>Testing the POST endpoint</h2>

                    <h3>1. Using curl</h3>
                    <pre>curl -X POST http://127.0.0.1:8000/hello \
  -H "Content-Type: application/json" \
  -d '{"name":"Rodrigo"}'</pre>


                    <p>Expected Output: <code>{"message": "Hello, Rodrigo! Timestamp: 2025-09-29T19:28:45.123456"}</code></p>
                    <p>Tip: get the output from "kubectl get svc" and change the endpoint address  </p>
                    <h3>2. Swagger documentation</h3>
                    <p>Check out <a href="/docs" target="_blank">/docs</a> for interactive API documentation where you can test endpoints easily.</p>

                    <h3>3. Test form</h3>
                    <div class="form-section">
                        
                        <form id="helloForm" onsubmit="sendPostRequest(event)">
                            <div class="form-group">
                                <label for="name">Your name:</label>
                                <input type="text" id="name" name="name" value="Rodrigo">
                            </div>
                            <button type="submit">Send Request</button>
                        </form>
                        
                        <div class="response-section">
                            <div class="response-label">Response:</div>
                            <div class="response-content" id="response">Waiting for request...</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <script>
                async function sendPostRequest(event) {
                    event.preventDefault();
                    const name = document.getElementById('name').value.trim();
                    const responseElement = document.getElementById('response');
                    
                    if (!name) {
                        responseElement.innerHTML = '<span class="error">⚠️ Please enter a name</span>';
                        return;
                    }
                    
                    responseElement.innerHTML = '⏳ Sending request...';
                    
                    try {
                        const response = await fetch('/hello', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ name: name })
                        });
                        
                        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                        
                        const data = await response.json();
                        responseElement.innerHTML = `<span class="success">✅ ${JSON.stringify(data, null, 2)}</span>`;
                    } catch (error) {
                        responseElement.innerHTML = `<span class="error">❌ Error: ${error.message}</span>`;
                    }
                }
                
                // Add some interactive features
                document.getElementById('name').addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        sendPostRequest(e);
                    }
                });
            </script>
        </body>
    </html>
    """




