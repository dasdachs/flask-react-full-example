export interface List {
  id: number;
  name: string;
  items: [];
}

export interface Items {
  id: number;
  name: string;
  quantity: number;
  min_quantity: number;
  category: Omit<Category, "items">;
  list: Omit<List, "items">;
}

export interface Category {
  id: number;
  name: string;
  items: Items;
}

export interface Token {
  access_token: string;
}
