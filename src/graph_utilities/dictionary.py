class Dictionary(object):
    def __init__(self, size=1000):
        self.size = size
        self.length = 0
        self.storage = []
        for _ in range(size):
            self.storage.append([])  # empty list of [key, value]

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        storage_idx = hash(key) % self.size
        exists = False

        # check if key already exists and update it
        for ele in self.storage[storage_idx]:
            if key == ele[0]:  # already exist, update it
                ele[1] = value
                exists = True
                break

        # if not exists, add new key value pair
        if not exists:
            self.storage[storage_idx].append([key, value])
            self.length += 1

    def __getitem__(self, key):
        storage_idx = hash(key) % self.size

        # search for the key in the storage
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                return ele[1]
        # if key not found, raise KeyError
        raise KeyError("Key {} dont exist".format(key))

    def __iterate_kv(self):
        for sub_lst in self.storage:
            # if it is empty list, continue
            if not sub_lst:
                continue

            # if it is not empty, iterate through the list and yield each item [key, value]
            for item in sub_lst:
                yield item

    def __iter__(self):
        # iterate over keys
        for key_var in self.__iterate_kv():
            yield key_var[0]

    def items(self):
        return self.__iterate_kv()

    def __str__(self):
        res = []
        for ele in self.storage:
            for key_value in ele:
                # check if the key is string or integer
                if isinstance(key_value[0], str):
                    key_str = "'{}'".format(key_value[0])
                else:
                    key_str = "{}".format(key_value[0])

                # check if the value is string or integer or array or another dictionary
                if isinstance(key_value[1], str):
                    value_str = "'{}'".format(key_value[1])
                elif isinstance(key_value[1], Dictionary):
                    value_str = str(key_value[1])
                elif isinstance(key_value[1], list):
                    value_str = "[{}]".format(
                        ", ".join(str(item) for item in key_value[1])
                    )
                else:
                    value_str = "{}".format(key_value[1])

                res.append("{}: {}".format(key_str, value_str))

        key_value_pairs_str = "{}".format(", ".join(res))
        return "{" + key_value_pairs_str + "}"

    def convert_to_str(self):
        return self.__str__()
