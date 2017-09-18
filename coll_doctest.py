def parse_inventory_item(string):
    '''String -> Item

    Return an inventory item encoded in the provided string.

    An Item is a dictionary of 3 elements:
        - name
        - price we paid
        - price we're charging

    The provided string seperates each of these pieces with a tab.

    >>> (parse_inventory_item('Coke\\t0.40\\t1.00') == 
    ...  {'name': 'Coke', 'paid': .4, 'charging': 1.0})
    True
    >>> (parse_inventory_item('Tab\\t0.54\\t1.49') ==
    ...  {'name': 'Tab', 'paid': 0.54, 'charging': 1.49})
    True
    '''
    menu = string.split('\t')
    return {'name': menu[0], 'paid': float(menu[1]), 'charging': float(menu[2])}

def read_inventory(string):
    '''String -> Dict[String, Item]

    Reads an inventory in from a provided string.
    Each line of the string represents a single inventory item formatted as described by `parse_into_inventory`.

    >>> read_inventory('')
    {}
    >>> (read_inventory('Coke\\t0.40\\t1.00\\nTab\\t0.54\\t1.49') ==
    ...  {'Coke': {'name': 'Coke', 'paid': .4, 'charging': 1.0},
    ...   'Tab': {'name': 'Tab', 'paid': 0.54, 'charging': 1.49}})
    True
    >>> (read_inventory('Chips\\t0.5\\t1.25\\nPizza\\t3.00\\t5.00\\nCoke\\t0.4\\t1.0') ==
    ...  {'Chips': {'name': 'Chips', 'paid': 0.5, 'charging': 1.25},
    ...   'Pizza': {'name': 'Pizza', 'paid': 3.0, 'charging': 5.0},
    ...   'Coke': {'name': 'Coke', 'paid': 0.4, 'charging': 1.0}})
    True
    '''
    d = {}
    for line in string.split('\n'):
        if line:
            item = parse_inventory_item(line)
            d[item['name']] = item
    return d

def profit(item):
    '''Item -> Float

    Returns the profit earned by selling the provided Item.

    >>> profit({'name': 'Coke', 'paid': 0.3, 'charging': 1.0})
    0.7
    >>> profit({'name': 'Tab', 'paid': 0.54, 'charging': 1.49})
    0.95
    '''
    return item['charging'] - item['paid']
    
def profits(items):
    '''List[Item] -> Float

    Returns the profit earned by selling all of the provided Items.

    >>> profits([])
    0.0
    >>> profits([{'name': 'Coke', 'paid': 0.3, 'charging': 1.0}])
    0.7
    >>> profits([
    ...   {'name': 'Coke', 'paid': 0.3, 'charging': 1.0},
    ...   {'name': 'Tab', 'paid': 0.54, 'charging': 1.49}])
    1.65
    '''
    amount = 0
    for item in items:
        amount += profit(item)
    return float(amount)   

def is_dollar_store(inventory):
    '''Dict[String, Item] -> Boolean

    Returns True if the provided inventory is a "dollar store".
    The store is a dollar store if all of its inventory costs $1 or less.

    >>> is_dollar_store({})
    True
    >>> is_dollar_store({
    ...   'Regular': {'name': 'Regular', 'price': 2.1, 'quantity': 500},
    ...   'Mid Grade': {'name': 'Mid Grade', 'price': 2.4, 'quantity': 350}, 
    ...   'Premium': {'name': 'Premium', 'price': 2.7, 'quantity': 400}})
    False
    >>> is_dollar_store({
    ...   'Apples': {'name': 'Apples', 'price': 2.1, 'quantity': 500}, 
    ...   'Bananas': {'name': 'Bananas', 'price': 2.4, 'quantiyt': 30}})
    False
    >>> is_dollar_store({
    ...   'Chips': {'name': 'Chips', 'price': .75, 'quantity': 24},
    ...   'Coke': {'name': 'Coke', 'price': .6, 'quantity': 12},
    ...   'Car': {'name': 'Car', 'price': 6000.0, 'quantity': 1}})
    False
    >>> is_dollar_store({
    ...   'Chips': {'name': 'Chips', 'price': .75, 'quantity': 24},
    ...   'Coke': {'name': 'Coke', 'price': .6, 'quantity': 12},
    ...   'Can': {'name': 'Can', 'price': .06, 'quantity': 1}})
    True
    '''
    for item in inventory:
        if inventory[item]['price'] >= 1:
            return False
    return True  

def find_item(inventory, item_name):
    '''(Dict[String, Item], String) -> Item

    Returns the Item with the provided item name.

    >>> (find_item({
    ...   'Regular': {'name': 'Regular', 'price': 2.1, 'quantity': 500},
    ...   'Mid Grade': {'name': 'Mid Grade', 'price': 2.4, 'quantity': 350}, 
    ...   'Premium': {'name': 'Premium', 'price': 2.7, 'quantity': 400}}, 'Regular') ==
    ...   {'name': 'Regular', 'price': 2.1, 'quantity': 500})
    True
    >>> (find_item({
    ...   'Regular': {'name': 'Regular', 'price': 2.1, 'quantity': 500},
    ...   'Mid Grade': {'name': 'Mid Grade', 'price': 2.4, 'quantity': 350}, 
    ...   'Premium': {'name': 'Premium', 'price': 2.7, 'quantity': 400}}, 'Premium') ==
    ...   {'name': 'Premium', 'price': 2.7, 'quantity': 400})
    True
    >>> (find_item({
    ...   'Chips': {'name': 'Chips', 'price': .75, 'quantity': 24},
    ...   'Coke': {'name': 'Coke', 'price': .6, 'quantity': 12},
    ...   'Can': {'name': 'Can', 'price': .06, 'quantity': 1}}, 'Coke') ==
    ...   {'name': 'Coke', 'price': .6, 'quantity': 12})
    True
    '''
    for item in inventory:
        if item == item_name:
            return (inventory[item])

def inventory_to_string(inventory):
    '''Dict[String, Item] -> String

    Returns a string representation of the provided inventory.
    The string format of the inventory is the same as the one provided to `read_inventory`
    The items should be written out in alphabetical order according to their names.

    >>> inventory_to_string({
    ...   'Coke': {'name': 'Coke', 'paid': .4, 'charging': 1.0},
    ...   'Tab': {'name': 'Tab', 'paid': 0.54, 'charging': 1.49}})
    'Coke\\t0.4\\t1.0\\nTab\\t0.54\\t1.49'
    >>> inventory_to_string({
    ...   'Chips': {'name': 'Chips', 'paid': 0.5, 'charging': 1.25},
    ...   'Pizza': {'name': 'Pizza', 'paid': 3.0, 'charging': 5.0},
    ...   'Coke': {'name': 'Coke', 'paid': 0.4, 'charging': 1.0}})
    'Chips\\t0.5\\t1.25\\nCoke\\t0.4\\t1.0\\nPizza\\t3.0\\t5.0'
    '''
    l = ''
    for value in sorted(inventory.values(), key=lambda i: i['name']):
        l += '{0}\t{1}\t{2}\n'.format(value['name'], value['paid'], value['charging'])
    return l.strip('\n')  
    