import React, {Ref, useEffect, useRef, useState} from 'react'
import './App.css'

import ContentBox from '../components/content-box/content-box'
import LoadBox from '../components/load-box/load-box'

function App() {
  const myStorage = window.localStorage

  const [isLoaded, setIsLoaded] = useState<boolean>(false)
  const [image, setImage] = useState<string>('')

  useEffect(() => {
    if (myStorage.hasOwnProperty('currImage')) {
      setIsLoaded(true)
      setImage(myStorage.getItem('currImage') || '')
    }
  }, [])

  //@ts-ignore
  const loadImage = (ref) => {
    let file = ref?.current.files[0];
    if (file) {
      const url = URL.createObjectURL(file)
      setImage(url)
      setIsLoaded(true)
      myStorage.setItem('currImage', url)
      if (ref?.current?.src) {
        // ref.current.src = url
      }
    }
  }

  const stopEdit = () => {
    setImage('')
    setIsLoaded(false)
    myStorage.removeItem('currImage')
  }

  return (
    <div className="App">
      {isLoaded
        ? <ContentBox stopEdit={stopEdit} image={image}/>
        : <LoadBox loadImage={loadImage}/>
      }
    </div>
  );
}

export default App
