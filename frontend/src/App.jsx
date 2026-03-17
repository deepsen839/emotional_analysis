import { useState } from "react"
import { predictEmotion } from "./api"

function App() {

  const [text,setText] = useState("")
  const [result,setResult] = useState(null)

  const handleSubmit = async () => {

    const payload = {
      journal_text: text,
      ambience_type: "ocean",
      duration_min: 20,
      sleep_hours: 7,
      energy_level: 3,
      stress_level: 2,
      time_of_day: "morning",
      previous_day_mood: "neutral",
      face_emotion_hint: "calm",
      reflection_quality: "high"
    }

    const prediction = await predictEmotion(payload)

    setResult(prediction)
  }

  return (

    <div style={{maxWidth:"800px",margin:"auto",padding:"40px"}}>

      <h1>Emotion Reflection AI</h1>

      <textarea
        rows="5"
        style={{width:"100%"}}
        placeholder="Write your reflection..."
        onChange={(e)=>setText(e.target.value)}
      />

      <br/><br/>

      <button onClick={handleSubmit}>
        Analyze Emotion
      </button>

      {result && (

        <div style={{marginTop:"30px"}}>

          <h2>Prediction</h2>

          <p><b>Emotion:</b> {result.predicted_state}</p>

          <p><b>Intensity:</b> {result.predicted_intensity}</p>

          <p><b>Confidence:</b> {result.confidence}</p>

          <p><b>Action:</b> {result.what_to_do}</p>

          <p><b>When:</b> {result.when_to_do}</p>

          <p><b>Message:</b> {result.supportive_message}</p>

        </div>

      )}

    </div>

  )
}

export default App