export async function base64ToURL(file: string) {
  const need = file.slice(3, file.length - 3)
  const base64Response = await fetch(`data:image/jpeg;base64,${need}`)
  const blob = await base64Response.blob()
  return URL.createObjectURL(blob)
}
