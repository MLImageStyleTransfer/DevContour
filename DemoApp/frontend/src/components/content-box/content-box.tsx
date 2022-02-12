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
        <h2 className={style.header}>Редактор</h2>
        <div className={style.imageWrapper}>
          {Boolean(image) && <img
              src={image}
              alt="fun"
              className={style.image}
          />}
        </div>
        <div className={style.manage}>
          <div className={`${style.customSize} input-group`}>
            <div className="input-group-prepend">
              <div className="input-group-text">
                <input type="checkbox" aria-label="Checkbox for following text input"/>
              </div>
            </div>
            <label className="form-control" aria-label="Text input with checkbox">
              Черно-белый фильтр
            </label>
          </div>
          <button
            onClick={stopEdit}
            className="btn btn-warning"
          >
            Отмена
          </button>
          <button
            onClick={stopEdit}
            className="btn btn-success"
          >
            Сохранить
          </button>
        </div>
      </div>
    </div>
  )
}