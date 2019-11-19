# DiskCache Task v1
## Description
Your aim is to write simulator of LRU cache for hard drive.
System provides availability for concurrent users to read and write key-value data.
Integers from 0 to 1000 can be used as keys in this task. Strings are used as values.

Data is physically stored on the group of hard drives. Each hard drive is split into blocks. In this task each drive is presented as file on the user’s machine. Blocks are written to files one by one. Each block has it’s address in format  `disk_no:block_no`.

Clients are working with disk via LRU cache.


## System Parts

### Config module

Reads config from `config.txt` file. Sets up variables for other modules.

### Disk Splitter module

Each "disk" is splitted into blocks of size `N`. Provides function `get_block(disk_no, block_no)` that gets data from disk block and `set_block(disk_no, block_no, value)` to write data on disk.

### LRU Cache module

Work with disk operations is done through LRU cache. Up to `M` blocks are loaded to the cache. Data is commited to disk only when block is dropped from LRU Cache.

provides `get_cached_block(disk_no, block_no)` and `set_cached_block(disk_no, block_no)` functions.

### Data Mapping module

Stores mapping from keys to sequence of blocks where value is stored. Also stores list of all free blocks. 
```
{
‘UNUSED_BLOCKS’: shuffled list of unused blocks,
Key1: list with addresses of blocks where data of ‘Key1’ is stored,
Key2: list with addresses of blocks where data of ‘Key2’ is stored,
…
}
```


### IO module

Provides end user with functions `write(key, text)` `read(key)` and `delete(key)` to create, update and delete values assigned to some keys. Values are splitted to blocks and written to files.

## Testing

To test itself system starts different threads that are performing some data. 
All actions are logged to console.

### Writer Thread
Writer thread generates random integer key, and tries to store under that key random poem from poems list.
### Reader Thread
Reader thread generates random integer key, and tries to read poem from those key and print it.
### Deleter Thread (optional)
Takes random key and tries to delete it.





## Configuration file example

```#/home/user/dk/config.txt
256  # block size in bytes
500  # number of blocks in each file
100  # blocks in LRU cache
16 # Readers threads running during test
5 # Writers threads running during test
2 # Deleters threads running during test
#Mappings file
/home/user/dk/disks/mappings.bytes
# Disks are listed one by one next
/home/user/dk/disks/disk1.bytes
/home/user/dk/disks/disk2.bytes
/home/user/dk/disks/disk3.bytes
/home/user/dk/disks/disk4.bytes
```



e
