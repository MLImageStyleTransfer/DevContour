import React, {useRef} from 'react'

type Props = {
  loadImage: (ref: any) => void
}

export default function LoadBox({loadImage}: Props) {
  const ref = useRef(null)

  return (
    <fieldset title="LOAD FORM">
      <input type="file" id="file" ref={ref}/>
      <button onClick={() => loadImage(ref)}>
        Save
      </button>
    </fieldset>
  )
}