def parse() -> list[str]:
    return list(open("input.txt", "r").readline().strip())


def part_1():
    def compute_checksum(ids: list):
        checksum = 0
        for i in range(len(ids)):
            if ids[i] == '.':
                continue
            checksum = checksum + ids[i] * i
        return checksum

    def compact(ids: list):
        start = 0
        end = len(ids) - 1

        while start < end:
            if ids[start] != '.':
                start = start + 1
                continue
            if ids[end] == '.':
                end = end - 1
                continue
            ids[start] = ids[end]
            ids[end] = '.'

    def convert_to_ids(disk_map: list[str]) -> list[str]:
        is_file = True
        current_id = 0
        ids = list()
        for i in range(len(disk_map)):
            if is_file:
                for j in range(int(disk_map[i])):
                    ids.append(current_id)
                current_id = current_id + 1
            else:
                for j in range(int(disk_map[i])):
                    ids.append('.')
            is_file = not is_file
        return ids

    disk_map = parse()
    ids = convert_to_ids(disk_map)
    compact(ids)
    print(compute_checksum(ids))


def part_2():
    def compute_checksum(ids: list):
        checksum = 0
        current_index = 0
        for i in range(len(ids)):
            for j in range(ids[i][0]):
                if ids[i][1] != -1:
                    checksum = checksum + ids[i][1] * current_index
                current_index = current_index + 1
        return checksum

    def compact(ids: list[tuple[int, int]]) -> list[tuple[int, int]]:
        right = len(ids)-1
        while right >= 0:
            if ids[right][1] == -1:
                if right != len(ids) - 1 and ids[right + 1][1] == -1:
                    ids = ids[:right] + [(ids[right][0] + ids[right + 1][0], -1)] + ids[right + 2:]
                right = right - 1
                continue

            for left in range(0 ,right):
                if ids[left][1] == -1 and ids[left][0] >= ids[right][0]:
                    new_nodes = [ids[right]] if ids[left][0] == ids[right][0] else [ids[right], (ids[left][0] - ids[right][0], -1)]
                    end_list = [(ids[right][0], -1)] if right == len(ids) - 1 else [(ids[right][0], -1)] + ids[right + 1:]
                    ids = ids[0:left] + new_nodes + ids[left + 1:right] + end_list
                    right = right + len(new_nodes)
                    break
            right = right - 1
        return ids

    def convert_to_ids(disk_map: list[str]) -> list[tuple[int, int]]:
        is_file = True
        current_id = 0
        ids = list()
        for i in range(len(disk_map)):
            if is_file:
                ids.append((int(disk_map[i]), current_id))
                current_id = current_id + 1
            else:
                ids.append((int(disk_map[i]), -1))
            is_file = not is_file
        return ids

    disk_map = parse()
    ids = convert_to_ids(disk_map)
    compacted_ids = compact(ids)
    print(compute_checksum(compacted_ids))

part_1()
part_2()
