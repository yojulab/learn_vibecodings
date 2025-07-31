import apiClient from './index';
import type { AxiosResponse } from 'axios';

// Pydantic 모델과 유사한 인터페이스를 정의합니다.
export interface Post {
  _id: string;
  title: string;
  content: string;
  category: string;
}

export interface PostCreate {
  title: string;
  content: string;
  category: string;
}

export interface PostUpdate {
  title?: string;
  content?: string;
  category?: string;
}

export const postsApi = {
  getPosts(): Promise<AxiosResponse<Post[]>> {
    return apiClient.get('/posts/');
  },
  getPost(id: string): Promise<AxiosResponse<Post>> {
    return apiClient.get(`/posts/${id}`);
  },
  createPost(data: PostCreate): Promise<AxiosResponse<Post>> {
    return apiClient.post('/posts/', data);
  },
  updatePost(id: string, data: PostUpdate): Promise<AxiosResponse<Post>> {
    return apiClient.put(`/posts/${id}`, data);
  },
  deletePost(id: string): Promise<AxiosResponse<void>> {
    return apiClient.delete(`/posts/${id}`);
  },
};
