import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import { getPost, deletePost } from '../services/api';

const PostDetailPage = () => {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!id) {
      setError('Invalid post ID');
      setLoading(false);
      return;
    }
    const fetchPost = async () => {
      try {
        const data = await getPost(id);
        setPost(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchPost();
  }, [id]);

  const handleDelete = async () => {
    if (window.confirm('Are you sure you want to delete this post?')) {
      try {
        await deletePost(id);
        // Redirect to home page after deletion
        window.location.href = '/';
      } catch (err) {
        setError(err.message);
      }
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!post) return <div>Post not found</div>;

  return (
    <div className="max-w-3xl mx-auto bg-white p-8 rounded-2xl shadow-lg mt-8">
      <h1 className="text-4xl font-extrabold mb-2 text-gray-900">{post.title}</h1>
      <p className="text-sm text-gray-500 mb-6">Category: <span className="font-medium text-blue-500">{post.category}</span></p>
      <div className="prose prose-lg max-w-none text-gray-800">
        <ReactMarkdown>{post.content}</ReactMarkdown>
      </div>
      <div className="mt-8 flex gap-2">
        <Link to={`/edit-post/${id}`} className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors duration-150">
          Edit
        </Link>
        <button onClick={handleDelete} className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600 transition-colors duration-150">
          Delete
        </button>
      </div>
    </div>
  );
};

export default PostDetailPage;
