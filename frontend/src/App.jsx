import React, { useEffect, useState } from 'react'

const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function App() {
  const [health, setHealth] = useState('loading...')
  useEffect(() => { fetch(API + '/health').then(r => r.json()).then(d => setHealth(d.status)).catch(() => setHealth('offline')) }, [])
  return (
    <div style={{ fontFamily:'Inter, system-ui, sans-serif', padding: 24 }}>
      <h1>AutoInfra Capital</h1>
      <p>Backend status: <strong>{health}</strong></p>
      <hr />
      <InvestorDemo />
    </div>
  )
}

function InvestorDemo(){
  const [name, setName] = useState('Test LP')
  const [email, setEmail] = useState('lp@example.com')
  const [created, setCreated] = useState(null)

  const create = async () => {
    const res = await fetch(API + '/v1/investors', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({ name, email }) })
    const data = await res.json(); setCreated(data)
  }

  return (
    <div>
      <h2>Investor Onboarding (demo)</h2>
      <input placeholder="Name" value={name} onChange={e=>setName(e.target.value)} />
      <input placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} />
      <button onClick={create}>Create</button>
      {created && <pre>{JSON.stringify(created, null, 2)}</pre>}
      <DealScoringDemo />
    </div>
  )
}

function DealScoringDemo(){
  const [resp, setResp] = useState(null)
  const score = async () => {
    const payload = {
      title: "Northern Cape 50MW Solar",
      sector: "energy",
      country: "ZA",
      capex: 500000000,
      cashflows: [-500000000, 90000000, 95000000, 100000000, 110000000, 120000000],
      esg_inputs: { environment: 80, social: 70, governance: 65 }
    }
    const r = await fetch((import.meta.env.VITE_API_BASE || 'http://localhost:8000') + '/v1/deals/score', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload) })
    setResp(await r.json())
  }
  return (
    <div style={{ marginTop: 24 }}>
      <h2>Deal Scoring (demo)</h2>
      <button onClick={score}>Score Sample Deal</button>
      {resp && <pre style={{ whiteSpace:'pre-wrap' }}>{JSON.stringify(resp, null, 2)}</pre>}
    </div>
  )
}
