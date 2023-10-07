import './App.css';
import { Header } from './components/header';

function App() {
  return (
    <>
    
      <div className="w-screen h-screen bg-navy-500">
        <div className='w-full h-1/6'/>
        <div className='w-full h-4/6'>
          <Header title="Hear How You Feel"/>
        </div>
        <div className='w-full h-1/6'/>
      </div>
    
    </>
  );
}

export default App;
