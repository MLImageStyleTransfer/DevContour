import React, {useEffect, useState} from 'react'
import './App.css'

import ContentBox from '../components/content-box/content-box'
import LoadBox from '../components/load-box/load-box'
import {Api} from '../api/api'
import {base64ToURL} from '../common/helpers/base64ToURL'

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
      console.log(file)
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

  const grayscaleTransform = () => {
    Api.recolor({image: image})
      .then(data => data.text())
      .then(async (file) => {
        const url = await base64ToURL(file)

        setImage(url)
        myStorage.setItem('currImage', url)
        console.log("OK")
      })
      .catch(error => {
        console.error(error)
      })
  }

  return (
    <div className="App">
      {isLoaded
        ? <ContentBox stopEdit={stopEdit}
                      image={image}
                      grayscaleTransform={grayscaleTransform}/>
        : <LoadBox loadImage={loadImage}/>
      }
    </div>
  );
}

export default App
