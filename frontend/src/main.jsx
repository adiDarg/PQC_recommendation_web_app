import { createRoot } from 'react-dom/client'
import './styles/index.css'
import App from './App.jsx'
import { Analytics } from "@vercel/analytics/next"

createRoot(document.getElementById('root')).render(
    <Analytics>
        <App />
    </Analytics>
)
