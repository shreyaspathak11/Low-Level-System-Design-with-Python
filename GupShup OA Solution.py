import sys

class SerializableHashMap:
    def __init__(self):
        self.page_size = 0
        self.num_pages = 0
        self.data = []

    def encode_int(self, value, buffer, offset):
        buffer[offset] = (value >> 24) & 0xFF
        buffer[offset + 1] = (value >> 16) & 0xFF
        buffer[offset + 2] = (value >> 8) & 0xFF
        buffer[offset + 3] = value & 0xFF

    def decode_int(self, buffer, offset):
        return (buffer[offset] << 24) | (buffer[offset + 1] << 16) | \
               (buffer[offset + 2] << 8) | buffer[offset + 3]

    def get_page_start(self, page_index):
        return 18 + page_index * self.page_size

    def search_key_in_page(self, key, page_index):
        start = self.get_page_start(page_index)
        for offset in range(0, self.page_size, 8):
            current_key = self.decode_int(self.data, start + offset)
            if current_key == key:
                return start + offset
            elif current_key == 0:
                break  # No more valid keys in this page
        return -1  # Key not found

    def init(self, page_size, num_pages):
        self.page_size = page_size
        self.num_pages = num_pages
        self.data = [0] * (18 + self.page_size * self.num_pages)
        self.encode_int(self.page_size, self.data, 0)
        self.encode_int(self.num_pages, self.data, 4)

    def get(self, key):
        if key == -1:
            if self.data[8] == 1:
                return self.decode_int(self.data, 9)
            else:
                return 0
        elif key == 0:
            if self.data[13] == 1:
                return self.decode_int(self.data, 14)
            else:
                return 0
        else:
            page_index = key % self.num_pages
            index = self.search_key_in_page(key, page_index)
            if index != -1:
                return self.decode_int(self.data, index + 4)
        return 0

    def put(self, key, value):
        if value == 0:
            return  # Values may never be 0
        if key == -1:
            self.data[8] = 1  # Set flag for key -1
            self.encode_int(value, self.data, 9)
        elif key == 0:
            self.data[13] = 1  # Set flag for key 0
            self.encode_int(value, self.data, 14)
        else:
            page_index = key % self.num_pages
            index = self.search_key_in_page(key, page_index)
            page_start = self.get_page_start(page_index)

            if index != -1:
                # Update existing key's value
                self.encode_int(value, self.data, index + 4)
            else:
                # Find first free slot
                for offset in range(0, self.page_size, 8):
                    current_key = self.decode_int(self.data, page_start + offset)
                    if current_key == 0 or current_key == -1:
                        self.encode_int(key, self.data, page_start + offset)
                        self.encode_int(value, self.data, page_start + offset + 4)
                        return
                raise Exception("No sufficient space in page")

    def delete(self, key):
        if key == -1:
            self.data[8] = 0  # Unset flag for key -1
            self.encode_int(0, self.data, 9)
        elif key == 0:
            self.data[13] = 0  # Unset flag for key 0
            self.encode_int(0, self.data, 14)
        else:
            page_index = key % self.num_pages
            index = self.search_key_in_page(key, page_index)
            if index != -1:
                self.encode_int(-1, self.data, index)
                self.encode_int(0, self.data, index + 4)

    def dump(self):
        os = []

        #(page size)
        os.append(f'{self.data[0]:02x}{self.data[1]:02x}{self.data[2]:02x}{self.data[3]:02x} ')

        #(number of pages)
        os.append(f'{self.data[4]:02x}{self.data[5]:02x}{self.data[6]:02x}{self.data[7]:02x} ')

        #following 10 bytes as separate 4-byte and 1-byte segments with 0s
        os.append('00 ')  # 1-byte flag
        os.append(f'{self.data[9]:02x}{self.data[10]:02x}{self.data[11]:02x}{self.data[12]:02x} ')  # 4-byte segment
        os.append('00 ')  # 1-byte flag
        os.append(f'{self.data[14]:02x}{self.data[15]:02x}{self.data[16]:02x}{self.data[17]:02x} ')  # 4-byte segment

        # each page content
        for page_index in range(self.num_pages):
            os.append("[")
            page_start = self.get_page_start(page_index)
            for offset in range(0, self.page_size, 8):
                key = self.decode_int(self.data, page_start + offset)
                value = self.decode_int(self.data, page_start + offset + 4)
                os.append(f'{key:08x}:{value:08x},')
            os.append("]")

        print("".join(os))

# if __name__ == "__main__":

    # input_data = sys.stdin.read()
    # commands = input_data.strip().splitlines()

    # hash_map = SerializableHashMap()

    # for command in commands:
    #     parts = command.split()
    #     cmd = parts[0]

    #     if cmd == 'init':
    #         page_size = int(parts[1])
    #         num_pages = int(parts[2])
    #         hash_map.init(page_size, num_pages)

    #     elif cmd == 'get':
    #         key = int(parts[1])
    #         print(hash_map.get(key))

    #     elif cmd == 'put':
    #         key = int(parts[1])
    #         value = int(parts[2])
    #         hash_map.put(key, value)

    #     elif cmd == 'delete':
    #         key = int(parts[1])
    #         hash_map.delete(key)

    #     elif cmd == 'dump':
    #         print(hash_map.dump())
# Example usage
hash_map = SerializableHashMap()
hash_map.init(16, 4)  
hash_map.put(12, 255)
hash_map.delete(1)
hash_map.get(1)
hash_map.dump()