def main():
    """Main code of program"""
    y: float = double(2.0)
    print(halve(y))
    
def halve(x:float) -> float:
    """Returns half of the value of x"""
    print(f"halve({x})")
    return x/2.0

def double(x:float) -> float:
    """Double a value"""
    print(f"double({x})")
    return x * 2.0

y: float = double(2.0)
print(halve(y))

if __name__ == "__main__":
    main()
