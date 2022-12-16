import React, { useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState([]);

  // useEffect(() => {
  //   fetch("/course").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data['course'])
  //       console.log(data)
  //     }
  //   )
  // })

  return (
    <div>
      {(typeof data == 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.map((course, i) => (
          <p key={i}>{course}</p>
        ))
      )}
    </div>
  )
}

export default App