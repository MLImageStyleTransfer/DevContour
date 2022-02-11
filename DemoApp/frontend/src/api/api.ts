import {config} from '../../config'

import {BASE_URL, RECOLOR_URL} from './constants'

import {RequestType} from './types'

export class Api {
  public static recolor(request: RequestType): Promise<any> {
    return fetch(Api.buildURL(), {
      method: 'GET',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(request)
    })
  }

  private static buildURL(): string {
    return `${BASE_URL}${config.port}${RECOLOR_URL}`
  }
}