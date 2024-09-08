from datetime import datetime, timedelta
import uuid

def timestamp_to_uuid(timestamp_str):
    # Define UUID epoch (October 15, 1582)
    UUID_EPOCH = datetime(1582, 10, 15, 0, 0, 0)
    
    # Parse the timestamp string
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
    
    # Calculate the difference from the UUID epoch
    delta = timestamp - UUID_EPOCH
    # Convert the difference to 100-nanosecond intervals
    timestamp_100ns = int(delta.total_seconds() * 1e7)
    
    # Convert to 60-bit representation
    time_low = timestamp_100ns & 0xFFFFFFFF
    time_mid = (timestamp_100ns >> 32) & 0xFFFF
    time_hi = (timestamp_100ns >> 48) & 0x0FFF
    
    # Construct the UUID
    uuid_str = (
        f"{time_low:08x}-"
        f"{time_mid:04x}-"
        f"{time_hi:04x}-"
        f"{'0000'}-"  # Placeholder for clock sequence and node
        f"{'000000000000'}"  # Placeholder for node (MAC address)
    )
    return uuid_str

# Example usage
timestamp_str = "2024-08-08 02:10:20.271848"
uuid_str = timestamp_to_uuid(timestamp_str)
print("UUID:", uuid_str)
