import React from 'react'

import style from './content-box.module.css'

type Props = {
  image?: string
  stopEdit: () => void
}

export default function ContentBox({image, stopEdit}: Props) {
  return (
    <div className={style.ground}>
      <div className={style.content}>
        <div className={style.imageWrapper}>
          {Boolean(image) && <img
              src={image}
              alt="fun"
              className={style.image}
          />}
        </div>
        <hr/>
        <br/>
        <button onClick={stopEdit}>
          Stop
        </button>
      </div>
    </div>
  )
}