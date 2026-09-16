import './App.css'
// import Button from './components/Button/Button.jsx'
// import { useState, useEffect } from "react";
// import Display from './components/Display/Display.jsx';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './pages/Home.jsx';
import SamplePage from './pages/SamplePage.jsx';

function App() {
  // const [count, setCount] = useState(0);

  // const handleClick = () => {
  //   setCount(count + 1);
  // }

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/sample-page' element={<SamplePage />} />
      </Routes>
    </BrowserRouter>
    
      // <>

      //   {/* <h1>Hello World</h1>
      //   <Button type="button" disabled={false} onClick={handleClick}>
      //     BUTTON
      //   </Button>
      //   <Display count={count}/> */}
      // </>
  )
}

export default App
