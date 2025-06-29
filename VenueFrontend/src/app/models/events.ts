export interface Event {
  E_id: string;
  name: string;
  genre: string;
  lineup: string[];      // from backend
  date: string;          // ISO format
  description: string;
  eimage: string;
  ticketUrl: string;
  status: string;
  V_id: string;
  min_price: number;
  max_price: number;
  currency: string;
}