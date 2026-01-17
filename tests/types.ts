// types.ts

export type AuthPayload = {
  token: string;
  user: {
    id: string;
    name: string;
    email: string;
    role: string;
  };
};

export type User = {
  id: string;
  name: string;
  email: string;
  role: string;
};

export type Product = {
  id: string;
  name: string;
  description: string;
  price: number;
};

export type CartItem = {
  id: string;
  quantity: number;
  product: Product;
};

export type Order = {
  id: string;
  userId: string;
  products: CartItem[];
  total: number;
  status: string;
};

export type Review = {
  id: string;
  productId: string;
  userId: string;
  rating: number;
  comment: string;
};