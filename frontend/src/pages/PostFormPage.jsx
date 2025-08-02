import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import MDEditor from '@uiw/react-md-editor';
import { getPost, createPost, updatePost } from '../services/api';

const PostFormPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const isEditing = Boolean(id);

  useEffect(() => {
    if (isEditing) {
      const fetchPost = async () => {
        setLoading(true);
        try {
          const data = await getPost(id);
          setTitle(data.title);
          setContent(data.content);
          setCategory(data.category);
        } catch (err) {
          setError(err.message);
        } finally {
          setLoading(false);
        }
      };
      fetchPost();
    }
  }, [id, isEditing]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const postData = { title, content, category };

    try {
      if (isEditing) {
        await updatePost(id, postData);
        navigate(`/posts/${id}`);
      } else {
        const newPost = await createPost(postData);
        navigate(`/posts/${newPost.id}`);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading && isEditing) return <div>Loading...</div>;

  return (
    <div className="max-w-2xl mx-auto bg-white p-8 rounded-2xl shadow-lg mt-8">
      <h1 className="text-3xl font-extrabold mb-6 text-gray-900">{isEditing ? 'Edit Post' : 'Create Post'}</h1>
      {error && <div className="text-red-500 mb-4">Error: {error}</div>}
      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label htmlFor="title" className="block text-gray-700 font-semibold mb-2">Title</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
            required
          />
        </div>
        <div>
          <label htmlFor="content" className="block text-gray-700 font-semibold mb-2">Content</label>
          <div className="prose max-w-none">
            <MDEditor
              value={content}
              onChange={setContent}
            />
          </div>
        </div>
        <div>
          <label htmlFor="category" className="block text-gray-700 font-semibold mb-2">Category</label>
          <input
            type="text"
            id="category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
            required
          />
        </div>
        <button
          type="submit"
          className="bg-green-500 text-white px-6 py-2 rounded-md hover:bg-green-600 transition-colors duration-150"
          disabled={loading}
        >
          {loading ? 'Saving...' : 'Save Post'}
        </button>
      </form>
    </div>
  );
};

export default PostFormPage;
