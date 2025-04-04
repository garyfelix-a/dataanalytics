def outer(name, second_name):
    def inner():
        def inner_inner():
            print(name,second_name)
        inner_inner()
    inner()
    
outer("Randy", "Ortan")