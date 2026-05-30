import { createRoot } from 'react-dom/client'
import './styles/index.css'
import App from './App.jsx'
import { Analytics } from "@vercel/analytics/next"
import { SpeedInsights } from "@vercel/speed-insights/next"

createRoot(document.getElementById('root')).render(
    <Analytics>
        <SpeedInsights>
            <App />
        </SpeedInsights>
    </Analytics>
)
