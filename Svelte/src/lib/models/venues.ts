export interface Venue {
  V_id: string;
  name: string;
  eventIds: string[];
  address: string;
  vimage?: string;
  longitude: number;
  latitude: number;
}