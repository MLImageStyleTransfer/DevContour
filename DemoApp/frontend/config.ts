import environment from 'dotenv'
import {DEFAULT_PORT} from './src/api/constants'
import {Config, RawConfig} from 'src/api/types'

export const config: Config = {
  port: (environment as RawConfig)?.PORT || DEFAULT_PORT
}