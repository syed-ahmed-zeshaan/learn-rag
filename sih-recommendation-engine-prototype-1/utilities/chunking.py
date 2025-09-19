def chunk_data(data,size):
    words=data.split();
    chunks=[];
    for i in range(0,len(words),size):
        chunks.append(" ".join(words[i:i+size]));
    return chunks;