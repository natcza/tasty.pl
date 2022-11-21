# Schemat modeli

``` mermaid
classDiagram
direction LR
Restaurant "*" <|..|> "*" Section : ManyToMany
Food "*" <|..|> "*" Section : ManyToMany
Restaurant "*" <|--|> "*" Kind : ManyToMany
class Restaurant{
    
    name
    city
    postcode
    street
    house_number
    phone_number
    gis
    rating -
    rating_counter - licznik rating
    delivery_time - czas dostawy
    delivery_price - koszt dostawy
    minimum_order_price - minimalna wartość zamówienia
    free_delivery - bezpłatna dostawa
}
class Food{
    name
    price
}

class Kind{
    name
}

class Section{
    name
    description
}    
```

``` mermaid
classDiagram
direction LR
Restaurant "*" <|..|> "*" Food : ManyToMany
Food "*" <|..|> "*" Section : ManyToMany
Restaurant "*" <|--|> "*" Kind : ManyToMany
class Restaurant{
    
    name
    city
    postcode
    street
    house_number
    phone_number
    gis
    rating -
    rating_counter - licznik rating
    delivery_time - czas dostawy
    delivery_price - koszt dostawy
    minimum_order_price - minimalna wartość zamówienia
    free_delivery - bezpłatna dostawa
}
class Food{
    name
    price
}

class Kind{
    name
}

class Section{
    name
    description
}    
```