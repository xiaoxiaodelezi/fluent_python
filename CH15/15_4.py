# 在with块之外使用LookingGlass类


class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please do not divide by zero!')
            return True


manager = LookingGlass()
print(manager)

monster = manager.__enter__()
print(monster == 'JABBERWOCKY')
print(monster)
print(manager)

manager.__exit__(None, None, None)
print(monster)
